# InsertDeleteFace Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertDeleteFace`

Inserts a DeleteFace feature.
Inserts a DeleteFace feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertDeleteFace( _
   ByVal Option As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Option As System.Integer
Dim value As System.Boolean
 
value = instance.InsertDeleteFace(Option)
```

```

System.bool InsertDeleteFace( 
   System.int Option
)
```

```

System.bool InsertDeleteFace( 
   System.int Option
) 
```

#### Parameters

*Option*
:   Option as defined in [swFaceDeleteOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaceDeleteOption_e.html)

#### Return Value

True if a DeleteFace feature is inserted, false if not

Remarks

This is a part-level operation and only works when the model is a [part document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md).

Example

[Insert and Change DeleteFace Feature (C#)](Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm)  
[Insert and Change DeleteFace Feature (VB.NET)](Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm)  
[Insert and Change DeleteFace Feature (VBA)](Insert_and_Change_DeleteFace_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.md)  
[IFeatureManager::EditDeleteFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditDeleteFace.md)
