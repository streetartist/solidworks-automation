# ReferenceComponent Property (IMateEntity2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceComponent`

Gets the reference component for this mate entity.
Gets the reference component for this mate entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferenceComponent As Component2
```

```

Dim instance As IMateEntity2
Dim value As Component2
 
value = instance.ReferenceComponent
```

```

Component2 ReferenceComponent {get;}
```

```

property Component2^ ReferenceComponent {
   Component2^ get();
}
```

#### Property Value

[Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

The component instance tree of a subassembly is not loaded because a subassembly does not have a view of its own. Thus, this property returns Nothing or null if the Inplace mate is in a subassembly.

Example

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)  
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)  
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)  
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)  
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.md)  
[IMateEntity2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.md)  
[IMateEntity2::Reference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~Reference.md)  
[IMateEntity2::ReferenceType2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceType2.md)
