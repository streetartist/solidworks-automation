# InsertPart3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart3`

Inserts the specified part in the specified configuration into this part.
Inserts the specified part in the specified configuration into this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertPart3( _
   ByVal FileName As System.String, _
   ByVal Options As System.Integer, _
   ByVal ConfigurationName As System.String _
) As Feature
```

```

Dim instance As IPartDoc
Dim FileName As System.String
Dim Options As System.Integer
Dim ConfigurationName As System.String
Dim value As Feature
 
value = instance.InsertPart3(FileName, Options, ConfigurationName)
```

```

Feature InsertPart3( 
   System.string FileName,
   System.int Options,
   System.string ConfigurationName
)
```

```

Feature^ InsertPart3( 
   System.String^ FileName,
   System.int Options,
   System.String^ ConfigurationName
) 
```

#### Parameters

*FileName*
:   Name of the part file to insert

*Options*
:   Insertion options as defined in [swInsertPartOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertPartOptions_e.html)

*ConfigurationName*
:   Name of FileName's configuration

#### Return Value

Inserted [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

This method inserts the specified part at the origin of this part. To position the inserted part at a different location or orientation or both, use [IFeatureManager::InsertMoveCopyBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.md).

Example

[Modify Derived Part (VBA)](Modify_Derived_Part_Example_VB.htm)  
[Modify Derived Part (VB.NET)](Modify_Derived_Part_Example_VBNET.htm)  
[Modify Derived Part (C#)](Modify_Derived_Part_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)
