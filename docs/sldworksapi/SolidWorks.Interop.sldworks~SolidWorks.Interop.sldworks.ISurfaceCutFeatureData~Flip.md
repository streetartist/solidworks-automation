# Flip Property (ISurfaceCutFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~Flip`

Gets or sets the flip setting for this surface cut.
Gets or sets the flip setting for this surface cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Flip As System.Boolean
```

```

Dim instance As ISurfaceCutFeatureData
Dim value As System.Boolean
 
instance.Flip = value
 
value = instance.Flip
```

```

System.bool Flip {get; set;}
```

```

property System.bool Flip {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the surface is flipped, false if not

Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData. See the examples for details.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Modify Surface-cut Feature (C#)](Modify_Surface_Cut_Feature_Example_CSharp.htm)  
[Modify Surface-cut Feature (VB.NET)](Modify_Surface_Cut_Feature_Example_VBNET.htm)  
[Modify Surface-cut Feature (VBA)](Modify_Surface_Cut_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.md)  
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.md)
