# InsertMultiFaceDraft Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMultiFaceDraft`

Inserts a multiface draft feature.
Inserts a multiface draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMultiFaceDraft( _
   ByVal Angle As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal EdgeDraft As System.Boolean, _
   ByVal PropType As System.Integer, _
   ByVal IsStepDraft As System.Boolean, _
   ByVal IsBodyDraft As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Angle As System.Double
Dim FlipDir As System.Boolean
Dim EdgeDraft As System.Boolean
Dim PropType As System.Integer
Dim IsStepDraft As System.Boolean
Dim IsBodyDraft As System.Boolean
Dim value As Feature
 
value = instance.InsertMultiFaceDraft(Angle, FlipDir, EdgeDraft, PropType, IsStepDraft, IsBodyDraft)
```

```

Feature InsertMultiFaceDraft( 
   System.double Angle,
   System.bool FlipDir,
   System.bool EdgeDraft,
   System.int PropType,
   System.bool IsStepDraft,
   System.bool IsBodyDraft
)
```

```

Feature^ InsertMultiFaceDraft( 
   System.double Angle,
   System.bool FlipDir,
   System.bool EdgeDraft,
   System.int PropType,
   System.bool IsStepDraft,
   System.bool IsBodyDraft
) 
```

#### Parameters

*Angle*
:   Draft angle in radians

*FlipDir*
:   True to flip the direction of the draft (the draft direction is determined by the  
    selected direction, which could be a planar face, a reference plane, an edge, or  
    two vertices; if you refer to the last argument in [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md),  
    then these items have a selection mark of 1; the faces to draft have a selection  
    mark of 2, and the draft edges have a selection mark of 4), false to not

*EdgeDraft*
:   True if this is an edge draft and the user selects edges to draft, false if this  
    is a face draft and the user selects faces to draft (SOLIDWORKS automatically selects  
    the faces next to the edge to be drafted)

*PropType*
:   Propagation type:

    - 0 = no propagation
    - 1 = propagate to the next tangent faces that share the base neutral plane; valid for edge draft or neutral plane draft
    - 2 = propagate to all faces that are a neighbor of the neutral plane
    - 3 = propagate to all faces that a neighbor of the neutral plane on all inner loops (for example, all faces of a pocket or a boss)
    - 4 = propagate to all faces that are a neighbor of the neutral plane on the outer loop (for example, the sides of a box with the bottom face as the neutral plane)

*IsStepDraft*
:   True if the draft is a step draft, false if not

*IsBodyDraft*
:   True if the draft is a body draft, false if not

#### Return Value

Pointer to the newly created draft [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Make the selections using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)
