# KeepInternalControlCurves Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~KeepInternalControlCurves`

Gets or sets whether to keep internal control curves for this surface-flatten feature.
Gets or sets whether to keep internal control curves for this surface-flatten feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepInternalControlCurves As System.Boolean
```

```

Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Boolean
 
instance.KeepInternalControlCurves = value
 
value = instance.KeepInternalControlCurves
```

```

System.bool KeepInternalControlCurves {get; set;}
```

```

property System.bool KeepInternalControlCurves {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to keep internal control curves, false to not

Example

[Get Data for Surface-flatten Feature (C#)](Get_Data_for_Surface_Flatten_Feature_Example_CSharp.htm)  
[Get Data for Surface-flatten Feature (VB.NET)](Get_Data_for_Surface_Flatten_Feature_Example_VBNET.htm)  
[Get Data for Surface-flatten Feature (VBA)](Get_Data_for_Surface_Flatten_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.md)  
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.md)
