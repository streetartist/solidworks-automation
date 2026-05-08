# IsAdvancedMate Property (IAngleMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~IsAdvancedMate`

Gets or sets whether this angle mate is a limit angle mate.
Gets or sets whether this angle mate is a limit angle mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsAdvancedMate As System.Boolean
```

```

Dim instance As IAngleMateFeatureData
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

True if a limit angle mate, false if a standard angle mate

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.md)  
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.md)
