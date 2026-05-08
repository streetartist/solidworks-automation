# SetName Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetName`

Sets the name of this annotation.
Sets the name of this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetName( _
   ByVal NameIn As System.String _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim NameIn As System.String
Dim value As System.Boolean
 
value = instance.SetName(NameIn)
```

```

System.bool SetName( 
   System.string NameIn
)
```

```

System.bool SetName( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   New and unique name for this annotation

#### Return Value

True if the name was successfully changed, false if the name was not successfully changed

Remarks

This method verifies that the name is unique before attempting to set the name.

Example

[Get and Set Name of Note (VBA)](Get_and_Set_Names_of_Note_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetName.md)
