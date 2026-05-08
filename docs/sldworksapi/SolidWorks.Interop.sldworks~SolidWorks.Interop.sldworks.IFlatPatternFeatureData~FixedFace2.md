# FixedFace2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~FixedFace2`

Gets or sets the fixed face of this Flat-Pattern feature.
Gets or sets the fixed face of this Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixedFace2 As System.Object
```

```

Dim instance As IFlatPatternFeatureData
Dim value As System.Object
 
instance.FixedFace2 = value
 
value = instance.FixedFace2
```

```

System.object FixedFace2 {get; set;}
```

```

property System.Object^ FixedFace2 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Fixed [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) (or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) for cylindrical sheet metal parts)

Remarks

The difference between this method and the now obsolete IFlatPatternFeatureData::FixedFace is that this method successfully returns the fixed face of a Flat-Pattern feature in a sheet metal part created in any version of SOLIDWORKS.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Get Fixed Face of Flat-Pattern Feature (VBA)](Get_Fixed_Face_of_Flat-Pattern_Feature_Example_VB.htm)  
[Get Fixed Face of Flat-Pattern Feature (VB.NET)](Get_Fixed_Face_of_Flat-Pattern_Feature_Example_VBNET.htm)  
[Get Fixed Face of Flat-Pattern Feature (C#)](Get_Fixed_Face_of_Flat-Pattern_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)
