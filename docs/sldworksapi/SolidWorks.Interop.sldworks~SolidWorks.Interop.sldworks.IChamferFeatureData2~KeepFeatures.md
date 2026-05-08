# KeepFeatures Property (IChamferFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~KeepFeatures`

Gets or sets whether to keep existing features on the entities selected for the chamfer.
Gets or sets whether to keep existing features on the entities selected for the chamfer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepFeatures As System.Boolean
```

```

Dim instance As IChamferFeatureData2
Dim value As System.Boolean
 
instance.KeepFeatures = value
 
value = instance.KeepFeatures
```

```

System.bool KeepFeatures {get; set;}
```

```

property System.bool KeepFeatures {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True keeps the existing features, false does not

Example

[Get Edge Chamfer Distances (C#)](Get_Edge_Chamfer_Distances_Example_CSharp.htm)  
[Get Edge Chamfer Distances (VB.NET)](Get_Edge_Chamfer_Distances_Example_VBNET.htm)  
[Get Edge Chamfer Distances (VBA)](Get_Edge_Chamfer_Distances_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.md)
