# CreateBodyFromFaces2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2`

Creates a temporary body from a list of faces.
Creates a temporary body from a list of faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBodyFromFaces2( _
   ByVal NumOfFaces As System.Integer, _
   ByVal Faces As System.Object, _
   ByVal ActionType As System.Integer, _
   ByVal DoLocalCheck As System.Boolean, _
   ByRef LocalCheckResult As System.Boolean _
) As System.Object
```

```

Dim instance As IModeler
Dim NumOfFaces As System.Integer
Dim Faces As System.Object
Dim ActionType As System.Integer
Dim DoLocalCheck As System.Boolean
Dim LocalCheckResult As System.Boolean
Dim value As System.Object
 
value = instance.CreateBodyFromFaces2(NumOfFaces, Faces, ActionType, DoLocalCheck, LocalCheckResult)
```

```

System.object CreateBodyFromFaces2( 
   System.int NumOfFaces,
   System.object Faces,
   System.int ActionType,
   System.bool DoLocalCheck,
   out System.bool LocalCheckResult
)
```

```

System.Object^ CreateBodyFromFaces2( 
   System.int NumOfFaces,
   System.Object^ Faces,
   System.int ActionType,
   System.bool DoLocalCheck,
   [Out] System.bool LocalCheckResult
) 
```

#### Parameters

*NumOfFaces*
:   Number of faces

*Faces*
:   Array of the [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

*ActionType*
:   Type of action as defined in [swCreateFacesBodyAction\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateFacesBodyAction_e.html)

*DoLocalCheck*
:   True to perform local checking on the resulting body, false to not

*LocalCheckResult*
:   If DoLocalCheck is True, then True if body is okay, false if not

#### Return Value

[Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) or NULL if the operation fails

Remarks

This method is useful when you attempt to copy a body with changes to that body. All of the input faces must be from the same body.

If you call this method to remove a hole, then the value that you specify for ActionType indicates to the modeler how to handle filling the hole. The result must be a solid.

This method is the opposite of [IBody2::DeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces3.md) or [IBody2::IDeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFaces3.md), which allows you to specify faces to remove.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.md)  
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.md)  
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.md)  
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.md)  
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md)  
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.md)  
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.md)  
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.md)  
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.md)  
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.md)  
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.md)  
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.md)  
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md)  
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md)  
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.md)
