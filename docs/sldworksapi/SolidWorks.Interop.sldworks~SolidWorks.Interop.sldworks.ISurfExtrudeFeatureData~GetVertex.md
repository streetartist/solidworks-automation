# GetVertex Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetVertex`

Gets the end condition vertex in the forward or reverse direction for this extruded surface.
Gets the end condition vertex in the forward or reverse direction for this extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVertex( _
   ByVal Forward As System.Boolean _
) As System.Object
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As System.Object
 
value = instance.GetVertex(Forward)
```

```

System.object GetVertex( 
   System.bool Forward
)
```

```

System.Object^ GetVertex( 
   System.bool Forward
) 
```

#### Parameters

*Forward*
:   True gets the vertex in the forward direction, false gets it in the reverse direction

#### Return Value

End condition [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::SetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetVertex.md)  
[ISurfExtrudeFeatureData::IGetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetVertex.md)  
[ISurfExtrudeFeatureData::ISetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetVertex.md)
