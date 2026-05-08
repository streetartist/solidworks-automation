# GetBodies2 Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetBodies2`

Gets the bodies in this part.
Gets the bodies in this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodies2( _
   ByVal BodyType As System.Integer, _
   ByVal BVisibleOnly As System.Boolean _
) As System.Object
```

```

Dim instance As IPartDoc
Dim BodyType As System.Integer
Dim BVisibleOnly As System.Boolean
Dim value As System.Object
 
value = instance.GetBodies2(BodyType, BVisibleOnly)
```

```

System.object GetBodies2( 
   System.int BodyType,
   System.bool BVisibleOnly
)
```

```

System.Object^ GetBodies2( 
   System.int BodyType,
   System.bool BVisibleOnly
) 
```

#### Parameters

*BodyType*
:   Type of body as defined in [swBodyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)

*BVisibleOnly*
:   True gets only the visible bodies, false gets all of the bodies in the part

#### Return Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

This method:

- Only supports solid and sheet (surface) body types.
- May vary the order in which bodies are returned.

Example

[Get Bodies (C++)](Get_Bodies_Example_CPlusPlus_COM.htm)  
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)  
[Set Body for Part (VB.NET)](Set_Body_for_View_Example_VBNET.htm)  
[Set Body for Part (VBA)](Set_Body_for_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IComponent2::GetBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies2.md)  
[IBodyFolder::GetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.md)  
[IBodyFolder::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~IGetBodies.md)
