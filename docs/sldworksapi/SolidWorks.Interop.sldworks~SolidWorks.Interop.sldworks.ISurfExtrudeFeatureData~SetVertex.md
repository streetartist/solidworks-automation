# SetVertex Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetVertex`

Sets the end condition vertex in the forward or reverse direction for this extruded surface.
Sets the end condition vertex in the forward or reverse direction for this extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetVertex( _
   ByVal Forward As System.Boolean, _
   ByVal Vtx As System.Object _
) 
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim Vtx As System.Object
 
instance.SetVertex(Forward, Vtx)
```

```

void SetVertex( 
   System.bool Forward,
   System.object Vtx
)
```

```

void SetVertex( 
   System.bool Forward,
   System.Object^ Vtx
) 
```

#### Parameters

*Forward*
:   True sets the vertex in the forward direction, false sets it in the reverse direction

*Vtx*
:   End condition [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::ISetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetVertex.md)  
[ISurfExtrudeFeatureData::GetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetVertex.md)  
[ISurfExtrudeFeatureData::IGetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetVertex.md)
