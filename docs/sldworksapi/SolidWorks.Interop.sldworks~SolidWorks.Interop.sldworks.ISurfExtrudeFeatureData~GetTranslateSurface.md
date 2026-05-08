# GetTranslateSurface Method (ISurfExtrudeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetTranslateSurface`

Gets the translate surface setting for this extruded surface.
Gets the translate surface setting for this extruded surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTranslateSurface( _
   ByVal Fwd As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISurfExtrudeFeatureData
Dim Fwd As System.Boolean
Dim value As System.Boolean
 
value = instance.GetTranslateSurface(Fwd)
```

```

System.bool GetTranslateSurface( 
   System.bool Fwd
)
```

```

System.bool GetTranslateSurface( 
   System.bool Fwd
) 
```

#### Parameters

*Fwd*
:   True gets the translate surface setting in the forward direction, false gets it in the reverse direction

#### Return Value

True if the translate surface setting is enabled, false if it is disabled

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
[ISurfTranslateFeatureData::SetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetTranslateSurface.md)
