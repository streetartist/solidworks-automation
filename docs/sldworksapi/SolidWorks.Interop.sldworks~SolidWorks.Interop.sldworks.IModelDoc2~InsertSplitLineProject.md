# InsertSplitLineProject Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineProject`

Splits a face by projecting sketch lines onto the face.
Splits a face by projecting sketch lines onto the face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSplitLineProject( _
   ByVal IsDirectional As System.Boolean, _
   ByVal FlipDir As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim IsDirectional As System.Boolean
Dim FlipDir As System.Boolean
 
instance.InsertSplitLineProject(IsDirectional, FlipDir)
```

```

void InsertSplitLineProject( 
   System.bool IsDirectional,
   System.bool FlipDir
)
```

```

void InsertSplitLineProject( 
   System.bool IsDirectional,
   System.bool FlipDir
) 
```

#### Parameters

*IsDirectional*
:   Whether to project in one direction:

    - 0 projects in both directions
    - 1 projects in one direction

*FlipDir*
:   Whether to project along the normal to the sketch plane; valid only when isDirectional = 1:

    - 0 projects in a direction opposite to the normal of the sketch plane
    - 1 projects along the normal of the sketch plane

Remarks

- The sketch to project must be selected using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with a mark value of 4.
- The faces to split must be selected using IModelDocExtension::SelectByID2 with mark values of 1.

Example

[Create Projection Split Line Feature (VBA)](Create_Projection_Split_Line_Example_VB.htm)  
[Create Projection Split Line Feature (VB.NET)](Create_Projection_Split_Line_Example_VBNET.htm)  
[Create Projection Split Line Feature (C#)](Create_Projection_Split_Line_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertSplitLineSil Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineSil.md)  
[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[IFeatureManager::InsertSplitLineIntersect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSplitLineIntersect.md)
