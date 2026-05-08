# AccuracyFactor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~AccuracyFactor`

Gets or sets the accuracy of the flattened triangle mesh.
Gets or sets the accuracy of the flattened triangle mesh.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AccuracyFactor As System.Integer
```

```

Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Integer
 
instance.AccuracyFactor = value
 
value = instance.AccuracyFactor
```

```

System.int AccuracyFactor {get; set;}
```

```

property System.int AccuracyFactor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

10 >= Accuracy of flattened triangle mesh >= 1; 1 is highest accuracy

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
