# SourceSketch Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData~SourceSketch`

Gets or sets the sketch for this wrap feature.
Gets or sets the sketch for this wrap feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SourceSketch As Sketch
```

```

Dim instance As IWrapSketchFeatureData
Dim value As Sketch
 
instance.SourceSketch = value
 
value = instance.SourceSketch
```

```

Sketch SourceSketch {get; set;}
```

```

property Sketch^ SourceSketch {
   Sketch^ get();
   void set (    Sketch^ value);
}
```

#### Property Value

[Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.md)  
[IWrapSketchFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData_members.md)
