# GetAutoFilletRadius Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletRadius`

Gets the automatic corner fillet radius for this thin feature.
Gets the automatic corner fillet radius for this thin feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAutoFilletRadius() As System.Double
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Double
 
value = instance.GetAutoFilletRadius()
```

```

System.double GetAutoFilletRadius()
```

```

System.double GetAutoFilletRadius(); 
```

#### Return Value

Fillet radius, if feature has automatic corner fillets enabled

Remarks

This method only applies to thin feature extrusions. If the feature is not a thin feature extrusion, then the return value is 0.0, and the COM version of this method returns S\_false in the status return value.

If the feature does not have automatic corner fillets enabled, then the return value is 0.0 and the COM version of this method returns S\_false in the status return value.

To get whether automatic corner fillet is enabled, use [IExtrudeFeatureData2::GetAutoFilletCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetAutoFilletCorners.md).  To set automatic fillets and radius, use [IExtrudeFeatureData2::SetAutoFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetAutoFillet.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IsThinFeature.md)
