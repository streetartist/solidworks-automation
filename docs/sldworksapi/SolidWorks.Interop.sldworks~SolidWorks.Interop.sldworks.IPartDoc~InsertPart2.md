# InsertPart2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart2`

Obsolete. Superseded by IPartDoc::InsertPart3.
Obsolete. Superseded by [IPartDoc::InsertPart3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertPart2( _
   ByVal FileName As System.String, _
   ByVal Options As System.Integer _
) As Feature
```

```

Dim instance As IPartDoc
Dim FileName As System.String
Dim Options As System.Integer
Dim value As Feature
 
value = instance.InsertPart2(FileName, Options)
```

```

Feature InsertPart2( 
   System.string FileName,
   System.int Options
)
```

```

Feature^ InsertPart2( 
   System.String^ FileName,
   System.int Options
) 
```

#### Parameters

*FileName*
:   Name of part file

*Options*
:   Insertion options as defined in [swInsertPartOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertPartOptions_e.html)

#### Return Value

Inserted [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

This method inserts the specified part at the origin of this part. To position the inserted part at a different location or orientation or both, use [IFeatureManager::InsertMoveCopyBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)
