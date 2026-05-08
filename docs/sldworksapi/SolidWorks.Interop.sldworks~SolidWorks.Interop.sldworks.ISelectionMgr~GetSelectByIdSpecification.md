# GetSelectByIdSpecification Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification`

Gets the selection specification for the specified object.
Gets the selection specification for the specified object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectByIdSpecification( _
   ByVal Object As System.Object, _
   ByRef SelectByString As System.String, _
   ByRef ObjectType As System.String, _
   ByRef Type As System.Integer _
) As System.Boolean
```

```

Dim instance As ISelectionMgr
Dim Object As System.Object
Dim SelectByString As System.String
Dim ObjectType As System.String
Dim Type As System.Integer
Dim value As System.Boolean
 
value = instance.GetSelectByIdSpecification(Object, SelectByString, ObjectType, Type)
```

```

System.bool GetSelectByIdSpecification( 
   System.object Object,
   out System.string SelectByString,
   out System.string ObjectType,
   out System.int Type
)
```

```

System.bool GetSelectByIdSpecification( 
   System.Object^ Object,
   [Out] System.String^ SelectByString,
   [Out] System.String^ ObjectType,
   [Out] System.int Type
) 
```

#### Parameters

*Object*
:   Object for which to get the selection specification

*SelectByString*
:   Feature name of Object; "" if Object is not a feature

*ObjectType*
:   Type of Object

*Type*
:   Type of Object as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

True if successful, false if not

Example

[Get Selection Specification (VBA)](Get_Selection_Specification_Example_VB.htm)  
[Get Selection Specification (VB.NET)](Get_Selection_Specification_Example_VBNET.htm)  
[Get Selection Specification (C#)](Get_Selection_Specification_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::GetSelectionSpecification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.md)  
[ISelectionMgr::GetSelectedObject6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md)  
[IModelDocExtension::SelectByID2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)  
[IFeature::GetNameForSelection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.md)  
[ISelectionMgr::GetSelectedObjectLoop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md)  
[ISelectionMgr::GetSelectedObjectMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.md)  
[ISelectionMgr::GetSelectedObjectsComponent4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4.md)  
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.md)  
[ISelectionMgr::GetSelectedObjectType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md)  
[ISelectionMgr::GetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.md)  
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.md)  
[ISelectionMgr::DeSelect2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.md)  
[ISelectionMgr::GetSelectedObjectMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.md)  
[ISelectionMgr::SetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.md)
