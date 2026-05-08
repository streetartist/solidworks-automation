# CopyWithMates2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CopyWithMates2`

Copies one or more components with mates in this assembly.
Copies one or more components with mates in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CopyWithMates2( _
   ByVal ComponentsToCopy As System.Object, _
   ByVal Repeat As System.Object, _
   ByVal NewEnityToMateTo As System.Object, _
   ByVal Values As System.Object, _
   ByVal FlipAlignment As System.Object, _
   ByVal FlipDimension As System.Object, _
   ByVal LockRotation As System.Object, _
   ByVal Orientation As System.Object _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim ComponentsToCopy As System.Object
Dim Repeat As System.Object
Dim NewEnityToMateTo As System.Object
Dim Values As System.Object
Dim FlipAlignment As System.Object
Dim FlipDimension As System.Object
Dim LockRotation As System.Object
Dim Orientation As System.Object
Dim value As System.Boolean
 
value = instance.CopyWithMates2(ComponentsToCopy, Repeat, NewEnityToMateTo, Values, FlipAlignment, FlipDimension, LockRotation, Orientation)
```

```

System.bool CopyWithMates2( 
   System.object ComponentsToCopy,
   System.object Repeat,
   System.object NewEnityToMateTo,
   System.object Values,
   System.object FlipAlignment,
   System.object FlipDimension,
   System.object LockRotation,
   System.object Orientation
)
```

```

System.bool CopyWithMates2( 
   System.Object^ ComponentsToCopy,
   System.Object^ Repeat,
   System.Object^ NewEnityToMateTo,
   System.Object^ Values,
   System.Object^ FlipAlignment,
   System.Object^ FlipDimension,
   System.Object^ LockRotation,
   System.Object^ Orientation
) 
```

#### Parameters

*ComponentsToCopy*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to copy

*Repeat*
:   Array of boolean values; each value indicates whether to use the existing mate reference for the corresponding component to copy; if true, copies the existing mate reference; if false, uses the corresponding entry in the NewEntityToMateTo array for the new mate reference

*NewEnityToMateTo*
:   Array of new mate references that map to the Repeat array; if an entry in the Repeat array is false, then the corresponding entry in this array is the new entity with which to mate the component to copy

*Values*
:   Array of distance or angle values for the mate references; specify distance in meters and angle in radians; valid for distance, angle, and profile center mates only

*FlipAlignment*
:   Array of booleans that map to the NewEntityToMateTo array; each value indicates the corresponding mate's alignment; true to flip alignment, false to not

*FlipDimension*
:   Array of booleans that map to the Values array; each value indicates the corresponding mate's distance; true for a positive distance dimension, false for a negative distance dimension; valid for distance, angle, and profile center mates only

*LockRotation*
:   Array of booleans that map to the NewEntityToMateTo array; true to prevent the components from rotating, false to allow the components to rotate; valid for concentric and profile center mates only

*Orientation*
:   Array of longs or integers that map to the Values array; each long or integer indicates the number of clicks in the user interface with which to orient the mate; a positive value indicates to orient the mate clockwise, a negative value indicates to orient the mate counterclockwise; valid for profile center mates only

#### Return Value

True if calling this method succeeded, false if it failed

Example

[Copy Component With Profile Center Mate (C#)](Copy_Component_With_Profile_Center_Mate_Example_CSharp.htm)  
[Copy Component With Profile Center Mate (VB.NET)](Copy_Component_With_Profile_Center_Mate_Example_VBNET.htm)  
[Copy Component With Profile Center Mate (VBA)](Copy_Component_With_Profile_Center_Mate_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddComponent5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5.md)  
[IAssemblyDoc::AddMate5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate5.md)
