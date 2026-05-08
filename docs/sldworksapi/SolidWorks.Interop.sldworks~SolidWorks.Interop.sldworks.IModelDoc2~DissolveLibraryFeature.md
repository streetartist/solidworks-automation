# DissolveLibraryFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DissolveLibraryFeature`

Dissolves the selected library features.
Dissolves the selected library features.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DissolveLibraryFeature() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.DissolveLibraryFeature()
```

```

System.bool DissolveLibraryFeature()
```

```

System.bool DissolveLibraryFeature(); 
```

#### Return Value

True if the selected library features are dissolved, false if not

Remarks

This method dissolves all library features that are selected when it executes. Only the selected library features are dissolved, anything else selected is ignored.

To create a library feature, use [IModelDoc2::InsertLibraryFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertLibraryFeature.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)
