# SetComponentsOrFacesToCheck Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetComponentsOrFacesToCheck`

Sets the components or faces for which to check clearances.
Sets the components or faces for which to check clearances.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetComponentsOrFacesToCheck( _
   ByVal Components As System.Object, _
   ByVal Faces As System.Object, _
   ByRef Errors As System.Integer _
) As System.Boolean
```

```

Dim instance As IClearanceVerificationMgr
Dim Components As System.Object
Dim Faces As System.Object
Dim Errors As System.Integer
Dim value As System.Boolean
 
value = instance.SetComponentsOrFacesToCheck(Components, Faces, Errors)
```

```

System.bool SetComponentsOrFacesToCheck( 
   System.object Components,
   System.object Faces,
   out System.int Errors
)
```

```

System.bool SetComponentsOrFacesToCheck( 
   System.Object^ Components,
   System.Object^ Faces,
   [Out] System.int Errors
) 
```

#### Parameters

*Components*
:   Array of [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s

*Faces*
:   Array of [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s

*Errors*
:   Error code as defined by [swClearanceVerificationSetEntityErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swClearanceVerificationSetEntityErrors_e.html)

#### Return Value

True if components and/or faces successfully set, false if not

Example

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md)  
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.md)
