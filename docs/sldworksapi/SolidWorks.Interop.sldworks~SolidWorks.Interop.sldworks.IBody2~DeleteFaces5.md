# DeleteFaces5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces5`

Deletes a set of faces from a temporary body.
Deletes a set of faces from a temporary body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteFaces5( _
   ByVal FaceList As System.Object, _
   ByVal HealAction As System.Integer, _
   ByVal LoopProcessOption As System.Integer, _
   ByVal DoLocalCheck As System.Boolean, _
   ByRef BodyList As System.Object, _
   ByRef LocalCheckResult As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBody2
Dim FaceList As System.Object
Dim HealAction As System.Integer
Dim LoopProcessOption As System.Integer
Dim DoLocalCheck As System.Boolean
Dim BodyList As System.Object
Dim LocalCheckResult As System.Boolean
Dim value As System.Boolean
 
value = instance.DeleteFaces5(FaceList, HealAction, LoopProcessOption, DoLocalCheck, BodyList, LocalCheckResult)
```

```

System.bool DeleteFaces5( 
   System.object FaceList,
   System.int HealAction,
   System.int LoopProcessOption,
   System.bool DoLocalCheck,
   out System.object BodyList,
   out System.bool LocalCheckResult
)
```

```

System.bool DeleteFaces5( 
   System.Object^ FaceList,
   System.int HealAction,
   System.int LoopProcessOption,
   System.bool DoLocalCheck,
   [Out] System.Object^ BodyList,
   [Out] System.bool LocalCheckResult
) 
```

#### Parameters

*FaceList*
:   Array containing the [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) for deletion

*HealAction*
:   Healing action as defined in [swHealActionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHealActionType_e.html) (see **Remarks**)

*LoopProcessOption*
:   Loop processing as defined in [swLoopProcessOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLoopProcessOption_e.html) (see **Remarks**)

*DoLocalCheck*
:   True checks the bodies during the operation and sets the return value to indicate whether the resultant body is valid, false does not

*BodyList*
:   Array of temporary [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*LocalCheckResult*
:   True if body is valid, false if not; to obtain this value, you must pass true for the DoLocalCheck argument

#### Return Value

True if set of faces are deleted, false if not

Remarks

When faces are deleted, wounds are created on those faces that require healing. Healing can be accomplished by extending neighboring faces, shrinking the deleted faces, or covering the wounds. The value that you specify for HealAction determines how wounds are healed.

When a wound has multiple loops, you can tell SOLIDWORKS how to process the loops individually or together, or you can let SOLIDWORKS decide how to process the loops. The value you specify for LoopProcessAction determines how to process multiple loops.

For example, consider a cube with a through hole made up of four faces (a square hole). To delete these four faces, specify swHealAction\_Shrink for HealAction and swLoopProcess\_Together for LoopProcessAction because the loop on the first face to be deleted is dependent on the loop of the second face to be deleted. Likewise, the loop on the second face to be deleted is dependent on the third face to be deleted, and so on.

Now consider the same cube with a through hole, except this through hole is a simple cylinder (one face). To delete the cylindrical face, specify swHealActionShrink\_e for HealAction and swLoopProcess\_Independent for LoopProcessAction to heal the loops independently. This is necessary because the cylindrical face actually has two loops (one at either end of the cylinder) that need to be healed separately.

It is possible to generate invalid geometry when you use this method because checking is disabled. Call [IBody2::Check3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3.md) to verify that the body is a valid solid after using this method.

|  |  |
| --- | --- |
| **swLoopProcess\_Together** | **swLoopProcess\_Independent** |
|  |  |

Example

[Create New Part from Existing Part Using Temporary Body (VB.NET)](Create_New_Part_from_Existing_Part_Using_Temporary_Body_Example_VBNET.htm)  
[Create New Part from Existing Part Using Temporary Body (VBA)](Create_New_Part_from_Existing_Part_Using_Temporary_Body_Example_VB.htm)  
[Create New Part from Existing Part Using Temporary Body (C#)](Create_New_Part_from_Existing_Part_Using_Temporary_Body_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::DeleteBlends3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends3.md)  
[IBody2::IDeleteBlends3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends3.md)  
[IBody2::EnumFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~EnumFaces.md)  
[IBody2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaceCount.md)  
[IBody2::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.md)  
[IBody2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFaces.md)  
[IBody2::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.md)
