# Position Property (ICallout)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~Position`

Gets and sets the position of this callout.
Gets and sets the position of this callout.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Position As MathPoint
```

```

Dim instance As ICallout
Dim value As MathPoint
 
instance.Position = value
 
value = instance.Position
```

```

MathPoint Position {get; set;}
```

```

property MathPoint^ Position {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

#### Property Value

[Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of this callout

Example

[Create a Callout Independent of a Selection (C#)](Create_a_Callout_Independent_of_a_Selection_Example_CSharp.htm)  
[Create a Callout Independent of a Selection (VB.NET)](Create_a_Callout_Independent_of_a_Selection_Example_VBNET.htm)  
[Create a Callout Independent of a Selection (VBA)](Create_a_Callout_Independent_of_a_Selection_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.md)  
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.md)  
[ICallout::GetTargetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~GetTargetPoint.md)  
[ICallout::SetTargetPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~SetTargetPoint.md)
