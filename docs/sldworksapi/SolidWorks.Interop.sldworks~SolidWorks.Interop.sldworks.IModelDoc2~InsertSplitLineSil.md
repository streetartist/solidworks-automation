# InsertSplitLineSil Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineSil`

Splits a face by creating split lines along the silhouette of the selected faces.
Splits a face by creating split lines along the silhouette of the selected faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSplitLineSil() 
```

```

Dim instance As IModelDoc2
 
instance.InsertSplitLineSil()
```

```

void InsertSplitLineSil()
```

```

void InsertSplitLineSil(); 
```

Remarks

The silhouette curves differ based on your orientation. Therefore, this method requires a selection to specify the desired direction.

Valid items to select to specify the direction are:

- reference plane
- planar face
- edge
- axis
- two points

The item selected for direction must be selected using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with a mark value of 2. The faces to split must be selected using IModelDocExtension::SelectByID2 with mark values of 1.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertSplitLineProject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineProject.md)  
[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[IFeatureManager::InsertSplitLineIntersect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSplitLineIntersect.md)
