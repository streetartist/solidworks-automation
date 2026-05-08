# InsertDeleteFace2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertDeleteFace2`

Obsolete. Superseded by IModelDocExtension::InsertDeleteFace.
Obsolete. Superseded by [IModelDocExtension::InsertDeleteFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertDeleteFace.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertDeleteFace2( _
   ByVal Refill As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Refill As System.Integer
Dim value As System.Boolean
 
value = instance.InsertDeleteFace2(Refill)
```

```

System.bool InsertDeleteFace2( 
   System.int Refill
)
```

```

System.bool InsertDeleteFace2( 
   System.int Refill
) 
```

#### Parameters

*Refill*
:   - 1 refills the face after it is deleted
    - 0 does not

#### Return Value

True if a [DeleteFace feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.md) is inserted in the model, false if not

Remarks

This is a part-level operation and only works when the model is a [IPartDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md).

Example

[Delete Selected Faces (VBA)](Delete_Selected_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IFeatureManager::EditDeleteFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditDeleteFace.md)
