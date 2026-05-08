# DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler`

Fired when the Large Design Review state changes in this assembly.
Fired when the Large Design Review state changes in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler( _
   ByVal PreviousState As System.Short, _
   ByVal newState As System.Short _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler( 
   System.short PreviousState,
   System.short newState
)
```

```

public delegate System.int DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler( 
   System.short PreviousState,
   System.short newState
)
```

#### Parameters

*PreviousState*
:   Old LDR state as defined by [swAssemblyMode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyMode_e.html)

*newState*
:   New LDR state as defined by swAssemblyMode\_e

Remarks

If developing a C++ application, use [swAssemblyLargeDesignReviewStateChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

'VBA

'=============================================================

'1. Create a VBA macro with the module code below.

'2. Copy the Class1 code below into a new Class1 module.

'3. Open an assembly

'4. Run the macro.

'5. In the user interface, change the LDR state of the assembly.

'6. A message box appears when the LDR state changes.

'==================================================

**'module**

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swDocSpecification As SldWorks.DocumentSpecification

Dim swAssemblyEvents As Class1

Dim swAssembly As SldWorks.AssemblyDoc

Option Explicit

Sub main()

    Set swApp = Application.SldWorks

    Set swModel = swApp.**ActiveDoc**

    Set swAssembly = swModel

   

    ' Set up event

    Set swAssemblyEvents = New Class1

    Set swAssemblyEvents.swAssembly = swAssembly

End Sub

**‘Class1 module**

Public WithEvents swAssembly As SldWorks.AssemblyDoc

Private Function swAssembly\_**LargeDesignReviewStateChangeNotify**(ByVal PreviousState As Integer, ByVal NewState As Integer) As Long

   

    If (PreviousState = swAssemblyMode\_LDR) Then

   

        If (NewState = swAssemblyMode\_LDR\_EditAssembly) Then

            MsgBox " Document state change from LDR to LDR Edit Assembly Mode", vbOKOnly, "LDR state change"

        ElseIf (NewState = swAssemblyMode\_LightWeight) Then

            MsgBox " Document state change from LDR to LightWeight Assembly Mode", vbOKOnly, "LDR state change"

        ElseIf (NewState = swAssemblyMode\_Resolved) Then

             MsgBox " Document state change from LDR to Resolve Assembly Mode", vbOKOnly, "LDR state change"

        Else

              MsgBox "Invalid Notification"

        End If

   

    ElseIf (PreviousState = swAssemblyMode\_LDR\_EditAssembly) Then

   

        If (NewState = swAssemblyMode\_LightWeight) Then

             MsgBox " Document state change from LDR Edit assembly to LightWeight Assembly Mode", vbOKOnly, "LDR state change"

        ElseIf (NewState = swAssemblyMode\_Resolved) Then

              MsgBox " Document state change from LDR Edit assembly to Resolve Assembly Mode", vbOKOnly, "LDR state change"

        Else

              MsgBox "Invalid notification"

        End If

   

    Else

         MsgBox "Invalid notification"

        

    End If

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_LargeDesignReviewStateChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LargeDesignReviewStateChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
