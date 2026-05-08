# IsFastener Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference~IsFastener`

Gets whether this interference includes a fastener or not.
Gets whether this interference includes a fastener or not.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsFastener As System.Boolean
```

```

Dim instance As IInterference
Dim value As System.Boolean
 
value = instance.IsFastener
```

```

System.bool IsFastener {get;}
```

```

property System.bool IsFastener {
   System.bool get();
}
```

#### Property Value

True if the interference includes a fastener, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.md)  
[IInterference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference_members.md)  
[IInterferenceDetectionMgr::CreateFastenersFolder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~CreateFastenersFolder.md)
