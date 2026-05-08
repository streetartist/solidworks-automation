# GetDepth Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetDepth`

Gets the depth of the feature in the forward or reverse direction.
Gets the depth of the feature in the forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDepth( _
   ByVal Forward As System.Boolean _
) As System.Double
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim value As System.Double
 
value = instance.GetDepth(Forward)
```

```

System.double GetDepth( 
   System.bool Forward
)
```

```

System.double GetDepth( 
   System.bool Forward
) 
```

#### Parameters

*Forward*
:   True gets the depth in the forward direction, false gets it in the reverse direction

#### Return Value

Extrusion depth

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.md)  
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.md)  
[ISurfExtrudeFeatureData::SetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetDepth.md)
