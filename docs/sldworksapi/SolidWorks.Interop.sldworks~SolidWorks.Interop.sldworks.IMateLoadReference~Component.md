# Component Property (IMateLoadReference)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~Component`

Gets the specified component associated with the mate that owns this load reference.
Gets the specified component associated with the mate that owns this load reference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Component( _
   ByVal WhichOne As System.Integer _
) As Component2
```

```

Dim instance As IMateLoadReference
Dim WhichOne As System.Integer
Dim value As Component2
 
value = instance.Component(WhichOne)
```

```

Component2 Component( 
   System.int WhichOne
) {get;}
```

```

property Component2^ Component {
   Component2^ get(System.int WhichOne);
}
```

#### Parameters

*WhichOne*
:   - 0 = Component1

    - 1 = Component2

#### Property Value

[Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) associated with the mate that owns this load reference

Example

[Insert Mate Load Reference (C#)](Insert_Mate_Load_Reference_Example_CSharp.htm)  
[Insert Mate Load Reference (VB.NET)](Insert_Mate_Load_Reference_Example_VBNET.htm)  
[Insert Mate Load Reference (VBA)](Insert_Mate_Load_Reference_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.md)  
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.md)
