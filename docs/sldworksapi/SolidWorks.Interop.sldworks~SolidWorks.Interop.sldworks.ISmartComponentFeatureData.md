# ISmartComponentFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData`

Allows access to a Smart Component.
Allows access to a Smart Component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISmartComponentFeatureData 
```

```

Dim instance As ISmartComponentFeatureData
```

```

public interface ISmartComponentFeatureData 
```

```

public interface class ISmartComponentFeatureData 
```

Remarks

A Smart Component is defined by:

- Components
- Features
- Feature references

A Smart Component is created in a training assembly. When the Smart Component is saved, it is saved with the training assembly in a SOLIDWORKS part.

When the Smart Component is inserted or edited in a target assembly, the training assembly opens in a small preview window, and the PropertyManager page of the Smart Component displays.

See the SOLIDWORKS Help for more information about Smart Components.

| Use... | To... |
| --- | --- |
| This interface | - Gain access to the training assembly of a Smart Component. - Gain access to the selection lists on the PropertyManager page of a Smart Component. - Insert features and components into a Smart Component. - Delete features and components from a Smart Component. |
| [IComponent2::GetSmartComponentData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData.md) | Get the current features, components, and feature references of a Smart Component. |
| [IComponent2::SetSmartComponentData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSmartComponentData.md) | Change which features and components to enable in a Smart Component and to insert Smart Features in a target assembly. |

Example

[Delete Smart Feature (VBA)](Delete_Smart_Feature_Example_VB.htm)  
[Delete Smart Feature (VB.NET)](Delete_Smart_Feature_Example_VBNET.htm)  
[Delete Smart Feature (C#)](Delete_Smart_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISmartComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IComponent2::IsSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent.md)
