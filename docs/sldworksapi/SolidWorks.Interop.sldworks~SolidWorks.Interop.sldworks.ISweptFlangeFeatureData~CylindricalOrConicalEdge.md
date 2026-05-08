# CylindricalOrConicalEdge Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~CylindricalOrConicalEdge`

Gets or sets the linear sketch entity to propagate to the flat pattern of this cylindrical or conical swept flange feature.
Gets or sets the linear sketch entity to propagate to the flat pattern of this cylindrical or conical swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CylindricalOrConicalEdge As System.Object
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Object
 
instance.CylindricalOrConicalEdge = value
 
value = instance.CylindricalOrConicalEdge
```

```

System.object CylindricalOrConicalEdge {get; set;}
```

```

property System.Object^ CylindricalOrConicalEdge {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Linear sketch entity

Remarks

This property is valid only:

- for cylindrical or conical swept flanges

    - and -

- for [sweep paths](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Path.md) that are sketches,

     - and -

- when not creating the swept flange on an existing sheet metal feature.

For more information, read the **SOLIDWORKS Help > Sheet Metal > Using Sheet Metal Tools > Swept Flange > Creating a Conical Body with a Swept Flange** topic.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)
