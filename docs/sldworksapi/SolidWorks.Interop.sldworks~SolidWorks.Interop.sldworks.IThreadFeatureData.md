# IThreadFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData`

Allows access to a thread feature.
Allows access to a thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IThreadFeatureData 
```

```

Dim instance As IThreadFeatureData
```

```

public interface IThreadFeatureData 
```

```

public interface class IThreadFeatureData 
```

Remarks

This interface:

- Accesses the feature data for a thread created either inside a cylindrical hole or around a cylindrical rod.
- Is functionally similar to the Thread PropertyManager in the SOLIDWORKS user interface.

To create a Thread feature, see [Thread Features and ThreadFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Thread_Features_and_ThreadFeatureData_Objects.htm).

For more information, see the **Thread PropertyManager** topic in the SOLIDWORKS user-interface help.

Example

[Create a Thread Feature (VBA)](Create_a_Thread_Feature_Example_VB.htm)  
[Create a Thread Feature (VB.NET)](Create_a_Thread_Feature_Example_VBNET.htm)  
[Create a Thread Feature (C#)](Create_a_Thread_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::CreateFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md)
