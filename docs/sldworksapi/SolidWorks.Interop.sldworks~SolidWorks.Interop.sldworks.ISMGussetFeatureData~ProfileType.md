# ProfileType Property (ISMGussetFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileType`

Gets or sets the type of profile of this gusset feature.
Gets or sets the type of profile of this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileType As System.Integer
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Integer
 
instance.ProfileType = value
 
value = instance.ProfileType
```

```

System.int ProfileType {get; set;}
```

```

property System.int ProfileType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of profile as defined in [swSheetMetalGussetProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalGussetProfileType_e.html)

Remarks

This property is valid only when editing an existing sheet metal gusset.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)
