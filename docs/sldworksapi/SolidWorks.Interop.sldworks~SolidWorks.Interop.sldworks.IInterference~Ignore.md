# Ignore Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~Ignore`

Gets or sets whether to ignore this interference.
Gets or sets whether to ignore this interference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Ignore As System.Boolean
```

```

Dim instance As IInterference
Dim value As System.Boolean
 
instance.Ignore = value
 
value = instance.Ignore
```

```

System.bool Ignore {get; set;}
```

```

property System.bool Ignore {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to ignore this interference, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.md)  
[IInterference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference_members.md)  
[IInterferenceDetectionMgr::ShowIgnoredInterferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ShowIgnoredInterferences.md)
