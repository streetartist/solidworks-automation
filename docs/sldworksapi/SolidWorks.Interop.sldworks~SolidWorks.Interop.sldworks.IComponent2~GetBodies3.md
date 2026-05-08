# GetBodies3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3`

Gets the bodies in this component.
Gets the bodies in this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBodies3( _
   ByVal BodyType As System.Integer, _
   ByRef BodiesInfo As System.Object _
) As System.Object
```

```

Dim instance As IComponent2
Dim BodyType As System.Integer
Dim BodiesInfo As System.Object
Dim value As System.Object
 
value = instance.GetBodies3(BodyType, BodiesInfo)
```

```

System.object GetBodies3( 
   System.int BodyType,
   out System.object BodiesInfo
)
```

```

System.Object^ GetBodies3( 
   System.int BodyType,
   [Out] System.Object^ BodiesInfo
) 
```

#### Parameters

*BodyType*
:   Type of body as defined by [swBodyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyType_e.html)

*BodiesInfo*
:   Array of information about the returned bodies as defined in [swBodyInfo\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyInfo_e.html)

#### Return Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) in the component

Remarks

This method:

- Only supports solid and surface bodies and part components,

- May vary the order in which bodies are returned,

- Supports lightweight components (the now obsolete IComponent2::GetBodies does not),

     - and -

- Returns an array in BodiesInfo containing information about bodies that indicates whether they are normal or user bodies. User bodies are original component bodies that have been modified in an assembly (e.g., a normal component body is cut in the assembly, resulting in two user component bodies). User bodies are not created for surface bodies.

Example

Also see the [IView::GetVisibleDrawingComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleDrawingComponents.md) examples.

Example

[Get Bodies in Components (C#)](Get_Bodies_in_Components_Example_CSharp.htm)  
[Get Bodies in Components (VB.NET)](Get_Bodies_in_Components_Example_VBNET.htm)  
[Get Bodies in Components (VBA)](Get_Bodies_in_Components_Example_VB.htm)  
[Get Bodies in Components (C++)](Get_Bodies_in_Components_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::EnumBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies2.md)  
[IComponent2::GetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.md)  
[IComponent2::IGetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBody.md)  
[IPartDoc::GetBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetBodies2.md)  
[IBody2::IsSheetMetal Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSheetMetal.md)
