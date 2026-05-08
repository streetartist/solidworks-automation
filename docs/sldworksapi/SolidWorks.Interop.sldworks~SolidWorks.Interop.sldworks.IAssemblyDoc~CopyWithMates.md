# CopyWithMates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CopyWithMates`

Obsolete. Superseded by IAssemblyDoc::CopyWithMates2.
Obsolete. Superseded by [IAssemblyDoc::CopyWithMates2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CopyWithMates2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CopyWithMates( _
   ByVal ComponentsToCopy As System.Object, _
   ByVal Repeat As System.Object, _
   ByVal NewEnityToMateTo As System.Object, _
   ByVal Values As System.Object, _
   ByVal FlipAlignment As System.Object _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim ComponentsToCopy As System.Object
Dim Repeat As System.Object
Dim NewEnityToMateTo As System.Object
Dim Values As System.Object
Dim FlipAlignment As System.Object
Dim value As System.Boolean
 
value = instance.CopyWithMates(ComponentsToCopy, Repeat, NewEnityToMateTo, Values, FlipAlignment)
```

```

System.bool CopyWithMates( 
   System.object ComponentsToCopy,
   System.object Repeat,
   System.object NewEnityToMateTo,
   System.object Values,
   System.object FlipAlignment
)
```

```

System.bool CopyWithMates( 
   System.Object^ ComponentsToCopy,
   System.Object^ Repeat,
   System.Object^ NewEnityToMateTo,
   System.Object^ Values,
   System.Object^ FlipAlignment
) 
```

#### Parameters

*ComponentsToCopy*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to copy

*Repeat*
:   Array of boolean values; each value indicates whether to use the existing mate reference for the corresponding component to copy: if true, copies the existing mate reference; if false, uses the corresponding entry in the NewEntityToMateTo array for the new mate reference

*NewEnityToMateTo*
:   Array of new mate references that map to the Repeat arrays; if an entry in the Repeat array is false, then the corresponding entry in this array is the new entity with which to mate the component to copy

*Values*
:   Array of distance or angle values for the mate references; specify distance in meters and angle in radians; valid for for distance and angle mates only

*FlipAlignment*
:   Array of booleans that map to the NewEntityToMateTo array; each value indicates the corresponding mate's alignment; true to flip alignment, false otherwise; valid for distance and angle mates only

#### Return Value

True if calling this method succeeded; false if it failed

Example

[Copy Components With Mates to Assembly (VBA)](Copy_Components_With_Mates_To_Assembly_Example_VB.htm)  
[Copy Components With Mates to Assembly (VB.NET)](Copy_Components_With_Mates_To_Assembly_Example_VBNET.htm)  
[Copy Components With Mates to Assembly (C#)](Copy_Components_With_Mates_To_Assembly_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
