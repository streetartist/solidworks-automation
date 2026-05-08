# GetFeatureCount Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFeatureCount`

Gets the number of features in this body in a multibody sheet metal part.
Gets the number of features in this body in a multibody sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureCount() As System.Integer
```

```

Dim instance As IBody2
Dim value As System.Integer
 
value = instance.GetFeatureCount()
```

```

System.int GetFeatureCount()
```

```

System.int GetFeatureCount(); 
```

#### Return Value

Number of features in this body

Remarks

The features of a body in a multibody sheet metal part are located in the solid bodies folder in the FeatureManager design tree.

Example

[Get Features of Multibody Sheet Metal Part (C#)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_CSharp.htm)  
[Get Features of Multibody Sheet Metal Part (VB.NET)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VBNET.htm)  
[Get Features of Multibody Sheet Metal Part (VBA)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFeatures.md)  
[IBody2::IGetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFeatures.md)  
[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md)  
[IBodyFolder::GetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.md)  
[IBodyFolder::GetBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodyCount.md)  
[IBodyFolder::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~IGetBodies.md)
