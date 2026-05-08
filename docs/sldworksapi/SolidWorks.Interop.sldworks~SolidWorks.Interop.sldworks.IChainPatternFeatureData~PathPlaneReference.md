# PathPlaneReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~PathPlaneReference`

Gets or sets the reference plane for the path selected for this chain pattern feature.
Gets or sets the reference plane for the [path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Path.md) selected for this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PathPlaneReference As System.Object
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Object
 
instance.PathPlaneReference = value
 
value = instance.PathPlaneReference
```

```

System.object PathPlaneReference {get; set;}
```

```

property System.Object^ PathPlaneReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Reference plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Remarks

This property is:

- only available when the path is a [sketch line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md).
- available for all types of chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)
