# GetFaceTangentTo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~GetFaceTangentTo`

Gets the tangent face for the specified loop where to create the patch.
Gets the tangent face for the specified loop where to create the patch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFaceTangentTo( _
   ByVal Index As System.Integer _
) As Face2
```

```

Dim instance As IShutOffSurfaceFeatureData
Dim Index As System.Integer
Dim value As Face2
 
value = instance.GetFaceTangentTo(Index)
```

```

Face2 GetFaceTangentTo( 
   System.int Index
)
```

```

Face2^ GetFaceTangentTo( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index for the loop where to create the patch

#### Return Value

[Tangent face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

This method is only available when the type of patch is set to swPatchTypeTangent. See [IShutOffSurfaceFeatureData::LoopPatchType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.md) and [IShutOffSurfaceFeatureData::SetAllPatchTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.md)  
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.md)  
[IShutOffSurfaceFeatureData::FlipFaceTangentTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~FlipFaceTangentTo.md)
