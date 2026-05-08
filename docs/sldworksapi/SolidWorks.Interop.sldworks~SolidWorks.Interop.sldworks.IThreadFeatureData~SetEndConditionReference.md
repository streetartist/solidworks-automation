# SetEndConditionReference Method (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~SetEndConditionReference`

Sets the Up To Selection end condition reference of this thread feature.
Sets the Up To Selection end condition reference of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEndConditionReference( _
   ByVal Value As System.Object _
) 
```

```

Dim instance As IThreadFeatureData
Dim Value As System.Object
 
instance.SetEndConditionReference(Value)
```

```

void SetEndConditionReference( 
   System.object Value
)
```

```

void SetEndConditionReference( 
   System.Object^ Value
) 
```

#### Parameters

*Value*
:   [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), or planar [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) (see **Remarks**)

Remarks

This method is valid only if [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.md) is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html).swEndCondUpToSelection.

Use [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) with Mark = 1 to select the end condition reference.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)  
[IThreadFeatureData::GetEndConditionReference Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~GetEndConditionReference.md)
