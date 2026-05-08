# ICThread Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread`

Allows access to a cosmetic thread.
Allows access to a cosmetic thread.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICThread 
```

```

Dim instance As ICThread
```

```

public interface ICThread 
```

```

public interface class ICThread 
```

Remarks

A cosmetic thread annotation in a drawing is typically associated with a cosmetic thread feature in the underlying model. The name of the annotation is the same as the name of the feature.

Use:

1. [IAnnotation::GetName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetName.md) to get the name of the CThread annotation in the drawing.
2. [IPartDoc::FeatureByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureByName.md) or [IPartDoc::IFeatureByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureByName.md) with that name, to get that feature in the model.
3. [ICosmeticThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md) to access the cosmetic thread model data once you have the feature.

Example

[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::HasLegacyCThreads Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasLegacyCThreads.md)
