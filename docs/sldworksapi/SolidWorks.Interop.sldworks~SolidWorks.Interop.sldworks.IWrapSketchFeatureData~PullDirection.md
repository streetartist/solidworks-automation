# PullDirection Property (IWrapSketchFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData~PullDirection`

Gets or sets the pull direction for this wrap feature.
Gets or sets the pull direction for this wrap feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PullDirection As System.Object
```

```

Dim instance As IWrapSketchFeatureData
Dim value As System.Object
 
instance.PullDirection = value
 
value = instance.PullDirection
```

```

System.object PullDirection {get; set;}
```

```

property System.Object^ PullDirection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Pointer one of the following entities as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

- swSelDATUMAXES
- swSelDATUMPLANES
- swSelEDGES
- swSelEXTSKETCHPOINTS
- swSelEXTSKETCHSEGS
- swSelFACES
- swSelLOCATIONS

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.md)  
[IWrapSketchFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData_members.md)
