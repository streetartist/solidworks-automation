# IsAdvancedMate Property (IDistanceMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~IsAdvancedMate`

Gets or sets whether this distance mate is a limit distance mate.
Gets or sets whether this distance mate is a limit distance mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsAdvancedMate As System.Boolean
```

```

Dim instance As IDistanceMateFeatureData
Dim value As System.Boolean
 
instance.IsAdvancedMate = value
 
value = instance.IsAdvancedMate
```

```

System.bool IsAdvancedMate {get; set;}
```

```

property System.bool IsAdvancedMate {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if a limit distance mate, false if a standard distance mate

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDistanceMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md)  
[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.md)
