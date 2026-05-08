# Centerline Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Centerline`

Gets and sets the centerline for this loft feature.
Gets and sets the centerline for this loft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Centerline As System.Object
```

```

Dim instance As ILoftFeatureData
Dim value As System.Object
 
instance.Centerline = value
 
value = instance.Centerline
```

```

System.object Centerline {get; set;}
```

```

property System.Object^ Centerline {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[ICenterLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.md)
