# IGetStack Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~IGetStack`

Gets the stacked notes in this balloon stack, excluding the master balloon.
Gets the stacked notes in this balloon stack, excluding the master balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetStack( _
   ByVal Count As System.Integer _
) As Note
```

```

Dim instance As IBalloonStack
Dim Count As System.Integer
Dim value As Note
 
value = instance.IGetStack(Count)
```

```

Note IGetStack( 
   System.int Count
)
```

```

Note^ IGetStack( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of balloons

#### Return Value

- in-process, unmanaged C++: Pointer to an array of stacked [notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) of size Count in the balloon stack

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Use [IBalloonStack::Count](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Count.md) to get the number of balloons in the balloon stack.

This method does not return the master balloon in the stack, only the other stacked notes. Use [IBalloonStack::Master](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Master.md) to get the master balloon of the stack.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.md)  
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.md)  
[IBalloonStack::Stack Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~Stack.md)
