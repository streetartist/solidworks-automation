# SetAutoFillet Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetAutoFillet`

Sets the automatic corner fillet properties of this thin feature.
Sets the automatic corner fillet properties of this thin feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAutoFillet( _
   ByVal AutoFillet As System.Boolean, _
   ByVal Radius As System.Double _
) As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim AutoFillet As System.Boolean
Dim Radius As System.Double
Dim value As System.Boolean
 
value = instance.SetAutoFillet(AutoFillet, Radius)
```

```

System.bool SetAutoFillet( 
   System.bool AutoFillet,
   System.double Radius
)
```

```

System.bool SetAutoFillet( 
   System.bool AutoFillet,
   System.double Radius
) 
```

#### Parameters

*AutoFillet*
:   True to fillet the corners automatically, false to not

*Radius*
:   Fillet radius, if automatic corner fillets is enabled

#### Return Value

True if the corners are automatically filleted, false if not

Remarks

This method only applies to thin feature extrusions. If the feature is not a thin feature extrusion, then no action is taken and the COM version of this method returns S\_false in the status return value.

If disabling the automatic corner fillets property (AutoFillet = false), then the Radius value is not used.

To get the automatic corner fillet flag, use [IExtrudeFeatureData2::GetAutoFilletCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletCorners.md). To get the fillet radius, use [IExtrudeFeatureData2::GetAutoFilletRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletRadius.md) .

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.md)
