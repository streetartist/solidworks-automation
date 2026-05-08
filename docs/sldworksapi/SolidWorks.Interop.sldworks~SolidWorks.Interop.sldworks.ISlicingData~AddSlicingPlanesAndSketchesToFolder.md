# AddSlicingPlanesAndSketchesToFolder Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~AddSlicingPlanesAndSketchesToFolder`

Gets or sets whether to add slicing planes and sketches to a folder in the FeatureManager design tree.
Gets or sets whether to add slicing planes and sketches to a folder in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AddSlicingPlanesAndSketchesToFolder As System.Boolean
```

```

Dim instance As ISlicingData
Dim value As System.Boolean
 
instance.AddSlicingPlanesAndSketchesToFolder = value
 
value = instance.AddSlicingPlanesAndSketchesToFolder
```

```

System.bool AddSlicingPlanesAndSketchesToFolder {get; set;}
```

```

property System.bool AddSlicingPlanesAndSketchesToFolder {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to add slicing planes and sketches to a folder in the FeatureManager design tree, false to not

Remarks

If this property is set to true, then after slicing, a **Slice1** folder is created in the FeatureManager design tree from which you can explicitly select and edit the slicing sketches and reference planes.

Example

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md)  
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.md)
