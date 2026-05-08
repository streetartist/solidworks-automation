# IMultiSelect Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IMultiSelect`

Obsolete. Superseded by IModelDocExtension::MultiSelect2.
Obsolete. Superseded by [IModelDocExtension::MultiSelect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMultiSelect( _
   ByVal Count As System.Integer, _
   ByRef Objects As System.Object, _
   ByVal AppendFlag As System.Boolean, _
   ByVal Data As SelectData _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim Objects As System.Object
Dim AppendFlag As System.Boolean
Dim Data As SelectData
Dim value As System.Integer
 
value = instance.IMultiSelect(Count, Objects, AppendFlag, Data)
```

```

System.int IMultiSelect( 
   System.int Count,
   ref System.object Objects,
   System.bool AppendFlag,
   SelectData Data
)
```

```

System.int IMultiSelect( 
   System.int Count,
   System.Object^% Objects,
   System.bool AppendFlag,
   SelectData^ Data
) 
```

#### Parameters

*Count*
:   Number of selectable objects

*Objects*
:   Array of selectable objects:

    - objects can be heterogeneous
    - if any object is not selected, then it is ignored

*AppendFlag*
:   True to append the objects to the selection list, false replace the current selection list with these objects

*Data*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

Number of objects selected

Remarks

If this now obsolete method is used to populate a selection box in a PropertyManager page, then [IPropertyManagerPage2Handler9::OnSubmitSelection](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSubmitSelection.md) only fires when set to true and [ISelectData::Mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Mark.md) is set to 0.

Use [IModelDocExtension::MultiSelect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect2.md) if you need IPropertyManagerPage2Handler9::OnSubmitSelection to fire when set to true and ISelectData::Mark is set to either a 0 or non-0 value.

The [Callout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Callout.md) property of the [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object is not used by this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::MultiSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect.md)  
[IModelDocExtension::SelectByID2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)  
[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.md)
