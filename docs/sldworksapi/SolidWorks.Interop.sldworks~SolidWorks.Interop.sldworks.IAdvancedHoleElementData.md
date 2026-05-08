# IAdvancedHoleElementData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData`

Allows access to Advanced Hole element data.
Allows access to Advanced Hole element data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IAdvancedHoleElementData 
```

```

Dim instance As IAdvancedHoleElementData
```

```

public interface IAdvancedHoleElementData 
```

```

public interface class IAdvancedHoleElementData 
```

Remarks

IAdvancedHoleElementData is extended by the following:

- [ICounterboreElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData.md)
- [ICountersinkElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.md)
- [IStraightElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.md)
- [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.md)
- [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.md)

After accessing the IAdvancedHoleElementData object, cast it to a hole type-specific object using one of the interfaces above and set the hole type-specific properties.

To create an Advanced Hole feature, see the [IFeatureManager::AdvancedHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole.md) Remarks.

Example

[Create Advanced Hole Feature (VBA)](Create_Advanced_Hole_Example_VB.htm)  
[Create Advanced Hole Feature (VB.NET)](Create_Advanced_Hole_Example_VBNET.htm)  
[Create Advanced Hole Feature (C#)](Create_Advanced_Hole_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.md)
