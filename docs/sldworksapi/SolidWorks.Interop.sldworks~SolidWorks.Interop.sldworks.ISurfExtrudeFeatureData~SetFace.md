# SetFace Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetFace`

Sets the end condition face for this extruded surface in the forward or reverse direction.
Sets the end condition face for this extruded surface in the forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFace( _
   ByVal Forward As System.Boolean, _
   ByVal Face As System.Object _
) 
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim Face As System.Object
 
instance.SetFace(Forward, Face)
```

```

void SetFace( 
   System.bool Forward,
   System.object Face
)
```

```

void SetFace( 
   System.bool Forward,
   System.Object^ Face
) 
```

#### Parameters

*Forward*
:   True sets the end condition face in the forward direction, false sets it in the reverse direction

*Face*
:   End condition [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::ISetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetFace.md)  
[ISurfExtrudeFeatureData::GetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetFace.md)  
[ISurfExtrudeFeatureData::IGetFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetFace.md)
