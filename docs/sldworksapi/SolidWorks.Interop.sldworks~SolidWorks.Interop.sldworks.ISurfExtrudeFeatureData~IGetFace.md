# IGetFace Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetFace`

Gets the end condition face for this extruded surface in the forward or reverse direction.
Gets the end condition face for this extruded surface in the forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFace( _
   ByVal Forward As System.Boolean _
) As Face2
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As Face2
 
value = instance.IGetFace(Forward)
```

```

Face2 IGetFace( 
   System.bool Forward
)
```

```

Face2^ IGetFace( 
   System.bool Forward
) 
```

#### Parameters

*Forward*
:   True gets the end condition face in the forward direction, false gets it in the reverse direction

#### Return Value

End condition [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::GetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetFace.md)  
[ISurfExtrudeFeatureData::ISetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetFace.md)  
[ISurfExtrudeFeatureData::SetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetFace.md)
