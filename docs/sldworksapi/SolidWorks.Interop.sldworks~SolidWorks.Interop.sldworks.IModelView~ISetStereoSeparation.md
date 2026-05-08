# ISetStereoSeparation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetStereoSeparation`

Obsolete and not superseded. Functionality no longer implemented.
Obsolete and not superseded. Functionality no longer implemented.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetStereoSeparation( _
   ByRef DfSeparation As System.Double _
) As System.Boolean
```

```

Dim instance As IModelView
Dim DfSeparation As System.Double
Dim value As System.Boolean
 
value = instance.ISetStereoSeparation(DfSeparation)
```

```

System.bool ISetStereoSeparation( 
   ref System.double DfSeparation
)
```

```

System.bool ISetStereoSeparation( 
   System.double% DfSeparation
) 
```

#### Parameters

*DfSeparation*
:   Array of 2 doubles representing the stereo magnitude and stereo parallax balance settings

#### Return Value

True if changing the stereo-value settings is successful, false if not

Remarks

This method only affects the model view's display if:

- Display window was set up to display stereoscopically
- Application is currently set to display stereoscopically.

[ISldWorks::EnableStereoDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableStereoDisplay.md) needs to be called to do these things.

There are two stereoscopic display values this method sets.

1. Settings[0] controls the magnitude of the stereoscopic effect by specifying the stereoscopic, virtual, camera separation. Appropriate values for this setting depend on the scale of the object, the distance from the virtual camera to the object center, the perspective field of view angle, and, perhaps, an adjustment factor that is available to the user.
2. Settings[1] controls the asymmetry of the projection frustums, thus, adjusting the parallax balance of the stereoscopic scene. It is desirable for any stereoscopic scene to comfortably balance the use of negative parallax (elements appearing to float in front of the display surface) and positive parallax (elements appearing to reside somewhere behind the display surface). Appropriate values for this setting should be arrived at experimentally.

If this method is not called, the default settings will equal 0.0, resulting in identical left-eye and right-eye renderings, and no visible stereo effect, even if stereoscopic display is currently enabled.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
